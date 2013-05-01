/**
 * This software was developed and / or modified by Raytheon Company,
 * pursuant to Contract DG133W-05-CQ-1067 with the US Government.
 * 
 * U.S. EXPORT CONTROLLED TECHNICAL DATA
 * This software product contains export-restricted data whose
 * export/transfer/disclosure is restricted by U.S. law. Dissemination
 * to non-U.S. persons whether in the United States or abroad requires
 * an export license or other authorization.
 * 
 * Contractor Name:        Raytheon Company
 * Contractor Address:     6825 Pine Street, Suite 340
 *                         Mail Stop B8
 *                         Omaha, NE 68106
 *                         402.291.0100
 * 
 * See the AWIPS II Master Rights File ("Master Rights File.pdf") for
 * further licensing information.
 **/
package com.raytheon.edex.plugin.redbook.common.blocks;

import java.nio.ByteBuffer;

/**
 * TODO Add Description
 * 
 * <pre>
 * 
 * SOFTWARE HISTORY
 * 
 * Date         Ticket#    Engineer    Description
 * ------------ ---------- ----------- --------------------------
 * 20080512           1131 jkorman     Initial implementation.
 * Apr 29, 2013 1958       bgonzale    Added class RedbookBlockHeader,
 *                                     and nested Factory class.
 * 
 * </pre>
 * 
 * @author jkorman
 * @version 1.0
 */

public class DefaultBlock extends RedbookBlock {

    public static class Factory implements RedbookBlockFactory {
        @Override
        public RedbookBlock createBlock(RedbookBlockHeader header,
                ByteBuffer data) {
            return new DefaultBlock(header, data);
        }
    }

    /**
     * 
     * @param header
     * @param separator
     */
    public DefaultBlock(RedbookBlockHeader header, ByteBuffer data) {
        super(header, data);
        if(hasLength()) {
            dropShortsFromTheBuffer(data);
        }
    }

    /**
     * 
     */
    public StringBuilder toString(StringBuilder sb) {
        sb = super.toString(sb);
        return sb;
    }
}
